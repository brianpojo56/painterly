import cv2
import painterly as pr

input_dir = "images/input/"
out_dir = "images/output/"


def paint_emma():
    file_name = "emma.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [16, 8, 4, 2]
    length = 200
    control_pt_distance = 1.0
    opacity = 0.8
    jitter = 5
    feathering = 4.0
    threshold = 60
    grid = 8

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + file_name, painterly.sketch)


def paint_beach():
    file_name = "beach.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [16, 8, 4, 2]
    length = 300
    control_pt_distance = 1
    opacity = 0.8
    jitter = 5
    feathering = 5.0
    threshold = 60
    grid = 16

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + file_name, painterly.sketch)


def paint_flamingo():
    file_name = "flamingo.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [8, 4, 4, 4, 2]
    length = 300
    control_pt_distance = 3.0
    opacity = 0.5
    jitter = 5
    feathering = 5.0
    threshold = 60
    grid = 16

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + file_name, painterly.sketch)


def paint_megaman():
    file_name = "megaman.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [16, 8, 4, 2]
    length = 300
    control_pt_distance = 2.0
    opacity = 0.7
    jitter = 10
    feathering = 5.0
    threshold = 60
    grid = 16

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + file_name, painterly.sketch)


def paint_rose():
    file_name = "rose.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [16, 8, 4, 2]
    length = 300
    control_pt_distance = 2.0
    opacity = 0.6
    jitter = 10
    feathering = 5.0
    threshold = 60
    grid = 16

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + file_name, painterly.sketch)


def paint_rose1():
    file_name = "rose.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [16, 2]
    length = 300
    control_pt_distance = 3.0
    opacity = 0.2
    jitter = 10
    feathering = 9.0
    threshold = 60
    grid = 16

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + "rose1.jpg", painterly.sketch)


def paint_rose2():
    file_name = "rose.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [8, 4, 2, 2]
    length = 300
    control_pt_distance = 3.0
    opacity = 0.9
    jitter = 5
    feathering = 1.0
    threshold = 35
    grid = 8

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + "rose2.jpg", painterly.sketch)


def paint_jj():
    file_name = "jj.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [16, 8, 4, 2]
    length = 300
    control_pt_distance = 3.0
    opacity = 0.8
    jitter = 5
    feathering = 1.0
    threshold = 35
    grid = 8

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + filename, painterly.sketch)


def paint_sunrise():
    file_name = "sunrise.jpg"
    image = cv2.imread(input_dir + file_name)
    brushes = [16, 8, 4, 2]
    length = 300
    control_pt_distance = 3.0
    opacity = 0.8
    jitter = 5
    feathering = 1.0
    threshold = 35
    grid = 8

    painterly = pr.Painterly(image, brushes, length, control_pt_distance,
                             opacity, jitter, feathering, threshold, grid)
    painterly.render(show_img=True)
    cv2.imwrite(out_dir + filename, painterly.sketch)


def main():
    #paint_emma()
    #paint_beach()
    #paint_megaman()
    #paint_rose()
    #paint_rose1()
    #paint_rose2()
    #paint_flamingo()
    #paint_jj()
    paint_sunrise()

if __name__ == "__main__":
    main()
