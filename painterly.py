import cv2
import numpy as np
from scipy import interpolate


class Painterly:

    def __init__(self, target_image, brush_sizes, max_length, ctl_point_dist,
                 paint_opacity, color_jitter, feathering, diff_threshold,
                 grid_spacing):
        self.R = brush_sizes
        self.L = max_length
        self.D = ctl_point_dist
        self.O = paint_opacity
        self.J = color_jitter
        self.F = feathering
        self.CT = diff_threshold
        self.G = grid_spacing

        self.image = target_image
        self.x_s = self.image.shape[1]
        self.y_s = self.image.shape[0]
        self.blurred = cv2.GaussianBlur(self.image, (5, 5), 0)
        gray = cv2.cvtColor(self.blurred, cv2.COLOR_RGB2GRAY)
        sobelx = -cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        self.theta = np.arctan(sobelx / (sobely + 0.00000000001))
        self.sketch = np.ones(self.image.shape, dtype=np.uint8) * 255

    def calc_control_points(self, (x, y), r):
        points = [(x, y)]
        moving = True
        start_color = self.image[y, x]
        angle = self.theta[y, x]
        while moving:
            try:
                prev_angle = self.theta[y, x]
                dx = np.cos(angle)
                dy = np.sin(angle)
                x += int(dx * r * self.D)
                y += int(dy * r * self.D)
                new_color = self.blurred[y, x]
                skt_color = self.sketch[y, x]
                angle = self.theta[y, x]
                if np.abs(angle - prev_angle) > np.abs(np.pi + angle - prev_angle):
                    angle += np.pi
                if len(points) >= (self.L / r * self.D):
                    #print "Max stroke length met"
                    moving = False
                elif self.rssd(start_color, new_color) > self.CT:
                    #print "Color difference threshold exceeded"
                    moving = False
                elif self.rssd(start_color, new_color) > self.rssd(start_color, skt_color):
                    #print "Sketch color is closer match"
                    moving = False
                else:
                    points.append((x, y))
            except:
                #print "Target index out of bounds"
                moving = False
        points = np.asarray(points)
        return points


    def get_curve(self, control_points):
        deg = 3
        if len(control_points) <= 3:
            deg = len(control_points) - 1
        if len(control_points) <= 1:
            return control_points
        tck, u = interpolate.splprep([control_points[:, 0], control_points[:, 1]], s = 0, k = deg)
        unew = np.arange(0, 1.01, 0.01)
        out = interpolate.splev(unew, tck)
        stroke = np.zeros((len(out[0]), 2), dtype=np.int32)
        stroke[:, 0] = out[0]
        stroke[:, 1] = out[1]
        return stroke


    def rssd(self, array1, array2):
        array1 = array1.astype(np.float64)
        array2 = array2.astype(np.float64)
        diff = np.sqrt(np.sum(np.power(array1 - array2, 2)))
        return diff


    def max_diff(self, image1, image2):
        img1 = cv2.cvtColor(image1.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float64)
        img2 = cv2.cvtColor(image2.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float64)
        difference = np.abs(img1 - img2)
        max_diff = np.where(difference == np.max(difference))
        idx = (max_diff[1][0], max_diff[0][0])
        if np.mean(difference) == np.max(difference):
            idx = (np.random.randint(img1.shape[1]), np.random.randint(img1.shape[0]))
        idx = (idx[1] - img1.shape[1] / 2, idx[0] - img1.shape[1] / 2)
        return idx


    def get_strokes(self, r):
        strokes = []
        offset = self.G / 2
        for i in range(offset, self.x_s - offset, self.G):
            for j in range(offset, self.y_s - offset, self.G):
                x = i
                y = j
                img_window, skc_window = self.get_windows(x, y, offset)
                dx, dy = self.max_diff(img_window, skc_window)
                x += dx
                y += dy
                strokes.append(self.calc_control_points((x, y), r))
        return strokes

    def paint_stroke(self, stroke, r):
        x, y = stroke[0, 0], stroke[0, 1]
        jitter = np.random.randint(-self.J, self.J + 1, 3)
        base_color = self.image[y, x].astype(np.int32) + jitter
        base_color[base_color < 0] = 0
        base_color[base_color > 255] = 255
        base_color = base_color.astype(np.uint8)
        temp = np.zeros(self.image.shape, dtype=np.float64)
        cv2.polylines(temp, [stroke], False, (1., 1., 1.), thickness= r * 2)
        temp = cv2.GaussianBlur(temp, (5, 5), self.F)
        temp = temp * self.O
        self.sketch = temp * base_color + (1 - temp) * self.sketch


    def get_windows(self, x, y, offset):
        print((y - offset, y + offset, x - offset, x + offset))
        img_window = self.image[y - offset: y + offset, x - offset: x + offset]
        skc_window = self.sketch[y - offset: y + offset, x - offset: x + offset]
        return img_window, skc_window


    def render(self, show_img = False):
        for r in self.R:
            strokes = self.get_strokes(r)
            for i in np.random.choice(len(strokes), len(strokes), replace=False):
                ctrl_pts = strokes[i]
                stroke = self.get_curve(ctrl_pts)
                self.paint_stroke(stroke, r)
                if show_img:
                    cv2.imshow('', self.sketch.astype(np.uint8))
                    cv2.waitKey(1)
