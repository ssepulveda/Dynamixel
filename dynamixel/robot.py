__author__ = 'ssepulveda'


class Robot:
    def __init__(self):
        """
        hombro_g_der = 1
        hombro_g_izq = 2
        hombro_l_der = 3
        hombro_l_izq = 4
        codo_der = 5
        codo_izq = 6
        pelvis_izq = 9
        pelvis_der = 10
        muslo_izq = 11
        muslo_der = 12
        rodilla_izq = 13
        rodilla_der = 14
        pie_f_izq = 15
        pie_f_der = 16
        pie_l_izq = 17
        pie_l_der = 18
        """

        self.shoulder = Component(1, 2)
        self.shoulder_vertical = Component(3, 4)
        self.elbow = Component(5, 6)
        self.hip = Component(9, 10)
        self.thigh = Component(11, 12)
        self.knee = Component(13, 14)
        self.foot_vertical = Component(15, 16)
        self.foot_horizontal = Component(17, 18)

        self.all = [
            self.shoulder.right, self.shoulder.left,
            self.shoulder_vertical.right, self.shoulder_vertical.left,
            self.elbow.right, self.elbow.left,
            self.hip.right, self.hip.left,
            self.thigh.right, self.thigh.left,
            self.knee.right, self.knee.left,
            self.foot_vertical.right, self.foot_vertical.left,
            self.foot_horizontal.right, self.foot_horizontal.left
            ]


class Component():
    def __init__(self, right, left):
        self.left = left
        self.right = right