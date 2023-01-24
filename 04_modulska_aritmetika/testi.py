from modulska_aritmetika import *
import unittest


class TestVsota(unittest.TestCase):
    def test_vsota_7(self):
        modul = 7
        z_7 = Zp(modul)
        resitev = [
            [0, 1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6, 0],
            [2, 3, 4, 5, 6, 0, 1],
            [3, 4, 5, 6, 0, 1, 2],
            [4, 5, 6, 0, 1, 2, 3],
            [5, 6, 0, 1, 2, 3, 4],
            [6, 0, 1, 2, 3, 4, 5]
        ]
        for i in range(modul):
            for j in range(modul):
                ans = z_7.vsota(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_7.vsota({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_vsota_3(self):
        modul = 3
        z_3 = Zp(modul)
        resitev = [
            [0, 1, 2],
            [1, 2, 0],
            [2, 0, 1]
        ]
        for i in range(modul):
            for j in range(modul):
                ans = z_3.vsota(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_3.vsota({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_vsota_29(self):
        modul = 29
        z_29 = Zp(modul)
        resitev = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1],
            [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2],
            [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3],
            [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4],
            [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5],
            [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6],
            [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7],
            [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8],
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
            [20, 21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [21, 22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [22, 23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
            [23, 24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
            [24, 25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
            [25, 26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            [26, 27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
            [27, 28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
            [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]]
        for i in range(modul):
            for j in range(modul):
                ans = z_29.vsota(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_29.vsota({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")


class TestZmnozek(unittest.TestCase):
    def test_zmnozek_7(self):
        modul = 7
        z_7 = Zp(modul)
        resitev = [[0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 2, 3, 4, 5, 6],
                   [0, 2, 4, 6, 1, 3, 5],
                   [0, 3, 6, 2, 5, 1, 4],
                   [0, 4, 1, 5, 2, 6, 3],
                   [0, 5, 3, 1, 6, 4, 2],
                   [0, 6, 5, 4, 3, 2, 1]]
        for i in range(modul):
            for j in range(modul):
                ans = z_7.zmnozek(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_7.zmnozek({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_zmnozek_3(self):
        modul = 3
        z_3 = Zp(modul)
        resitev = [[0, 0, 0],
                   [0, 1, 2],
                   [0, 2, 1]]
        for i in range(modul):
            for j in range(modul):
                ans = z_3.zmnozek(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_3.zmnozek({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_zmnozek_29(self):
        modul = 29
        z_29 = Zp(modul)
        resitev = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27],
            [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 2, 5, 8, 11, 14, 17, 20, 23, 26],
            [0, 4, 8, 12, 16, 20, 24, 28, 3, 7, 11, 15, 19, 23, 27, 2, 6, 10, 14, 18, 22, 26, 1, 5, 9, 13, 17, 21, 25],
            [0, 5, 10, 15, 20, 25, 1, 6, 11, 16, 21, 26, 2, 7, 12, 17, 22, 27, 3, 8, 13, 18, 23, 28, 4, 9, 14, 19, 24],
            [0, 6, 12, 18, 24, 1, 7, 13, 19, 25, 2, 8, 14, 20, 26, 3, 9, 15, 21, 27, 4, 10, 16, 22, 28, 5, 11, 17, 23],
            [0, 7, 14, 21, 28, 6, 13, 20, 27, 5, 12, 19, 26, 4, 11, 18, 25, 3, 10, 17, 24, 2, 9, 16, 23, 1, 8, 15, 22],
            [0, 8, 16, 24, 3, 11, 19, 27, 6, 14, 22, 1, 9, 17, 25, 4, 12, 20, 28, 7, 15, 23, 2, 10, 18, 26, 5, 13, 21],
            [0, 9, 18, 27, 7, 16, 25, 5, 14, 23, 3, 12, 21, 1, 10, 19, 28, 8, 17, 26, 6, 15, 24, 4, 13, 22, 2, 11, 20],
            [0, 10, 20, 1, 11, 21, 2, 12, 22, 3, 13, 23, 4, 14, 24, 5, 15, 25, 6, 16, 26, 7, 17, 27, 8, 18, 28, 9, 19],
            [0, 11, 22, 4, 15, 26, 8, 19, 1, 12, 23, 5, 16, 27, 9, 20, 2, 13, 24, 6, 17, 28, 10, 21, 3, 14, 25, 7, 18],
            [0, 12, 24, 7, 19, 2, 14, 26, 9, 21, 4, 16, 28, 11, 23, 6, 18, 1, 13, 25, 8, 20, 3, 15, 27, 10, 22, 5, 17],
            [0, 13, 26, 10, 23, 7, 20, 4, 17, 1, 14, 27, 11, 24, 8, 21, 5, 18, 2, 15, 28, 12, 25, 9, 22, 6, 19, 3, 16],
            [0, 14, 28, 13, 27, 12, 26, 11, 25, 10, 24, 9, 23, 8, 22, 7, 21, 6, 20, 5, 19, 4, 18, 3, 17, 2, 16, 1, 15],
            [0, 15, 1, 16, 2, 17, 3, 18, 4, 19, 5, 20, 6, 21, 7, 22, 8, 23, 9, 24, 10, 25, 11, 26, 12, 27, 13, 28, 14],
            [0, 16, 3, 19, 6, 22, 9, 25, 12, 28, 15, 2, 18, 5, 21, 8, 24, 11, 27, 14, 1, 17, 4, 20, 7, 23, 10, 26, 13],
            [0, 17, 5, 22, 10, 27, 15, 3, 20, 8, 25, 13, 1, 18, 6, 23, 11, 28, 16, 4, 21, 9, 26, 14, 2, 19, 7, 24, 12],
            [0, 18, 7, 25, 14, 3, 21, 10, 28, 17, 6, 24, 13, 2, 20, 9, 27, 16, 5, 23, 12, 1, 19, 8, 26, 15, 4, 22, 11],
            [0, 19, 9, 28, 18, 8, 27, 17, 7, 26, 16, 6, 25, 15, 5, 24, 14, 4, 23, 13, 3, 22, 12, 2, 21, 11, 1, 20, 10],
            [0, 20, 11, 2, 22, 13, 4, 24, 15, 6, 26, 17, 8, 28, 19, 10, 1, 21, 12, 3, 23, 14, 5, 25, 16, 7, 27, 18, 9],
            [0, 21, 13, 5, 26, 18, 10, 2, 23, 15, 7, 28, 20, 12, 4, 25, 17, 9, 1, 22, 14, 6, 27, 19, 11, 3, 24, 16, 8],
            [0, 22, 15, 8, 1, 23, 16, 9, 2, 24, 17, 10, 3, 25, 18, 11, 4, 26, 19, 12, 5, 27, 20, 13, 6, 28, 21, 14, 7],
            [0, 23, 17, 11, 5, 28, 22, 16, 10, 4, 27, 21, 15, 9, 3, 26, 20, 14, 8, 2, 25, 19, 13, 7, 1, 24, 18, 12, 6],
            [0, 24, 19, 14, 9, 4, 28, 23, 18, 13, 8, 3, 27, 22, 17, 12, 7, 2, 26, 21, 16, 11, 6, 1, 25, 20, 15, 10, 5],
            [0, 25, 21, 17, 13, 9, 5, 1, 26, 22, 18, 14, 10, 6, 2, 27, 23, 19, 15, 11, 7, 3, 28, 24, 20, 16, 12, 8, 4],
            [0, 26, 23, 20, 17, 14, 11, 8, 5, 2, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, 27, 24, 21, 18, 15, 12, 9, 6, 3],
            [0, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],
            [0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
        for i in range(modul):
            for j in range(modul):
                ans = z_29.zmnozek(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_29.zmnozek({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")


class TestNasprotno(unittest.TestCase):

    def test_nasprotno_3(self):
        modul = 3
        resitev = [0, 2, 1]
        z_3 = Zp(modul)
        for i in range(modul):
            ans = z_3.nasprotno(i)
            correct = resitev[i]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_3.nasprotno({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_nasprotno_7(self):
        modul = 7
        resitev = [0, 6, 5, 4, 3, 2, 1]
        z_7 = Zp(modul)
        for i in range(modul):
            ans = z_7.nasprotno(i)
            correct = resitev[i]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_7.nasprotno({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_nasprotno_29(self):
        modul = 29
        resitev = [0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3,
                   2, 1]
        z_29 = Zp(modul)
        for i in range(modul):
            ans = z_29.nasprotno(i)
            correct = resitev[i]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_29.nasprotno({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")


class TestRazlika(unittest.TestCase):
    def test_razlika_3(self):
        modul = 3
        resitev = [
            [0, 2, 1],
            [1, 0, 2],
            [2, 1, 0]
        ]
        z_3 = Zp(modul)
        for i in range(modul):
            for j in range(modul):
                ans = z_3.razlika(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_3.razlika({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_razlika_7(self):
        modul = 7
        resitev = [
            [0, 6, 5, 4, 3, 2, 1],
            [1, 0, 6, 5, 4, 3, 2],
            [2, 1, 0, 6, 5, 4, 3],
            [3, 2, 1, 0, 6, 5, 4],
            [4, 3, 2, 1, 0, 6, 5],
            [5, 4, 3, 2, 1, 0, 6],
            [6, 5, 4, 3, 2, 1, 0]]
        z_7 = Zp(modul)
        for i in range(modul):
            for j in range(modul):
                ans = z_7.razlika(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_7.razlika({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_razlika_29(self):
        modul = 29
        resitev = [
            [0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
            [2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
            [3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
            [4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
            [5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
            [6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7],
            [7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8],
            [8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
            [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12],
            [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13],
            [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14],
            [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15],
            [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16],
            [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17],
            [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18],
            [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19],
            [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21, 20],
            [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22, 21],
            [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23, 22],
            [22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24, 23],
            [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25, 24],
            [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26, 25],
            [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27, 26],
            [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28, 27],
            [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 28],
            [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
        z_29 = Zp(modul)
        for i in range(modul):
            for j in range(modul):
                ans = z_29.razlika(i, j)
                correct = resitev[i][j]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_29.razlika({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")


class TestObratno(unittest.TestCase):

    def test_obratno_3(self):
        modul = 3
        resitev = [1, 2]
        z_3 = Zp(modul)
        for i in range(1, modul):
            ans = z_3.obratno(i)
            correct = resitev[i - 1]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_3.obratno({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_obratno_7(self):
        modul = 7
        resitev = [1, 4, 5, 2, 3, 6]
        z_7 = Zp(modul)
        for i in range(1, modul):
            ans = z_7.obratno(i)
            correct = resitev[i - 1]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_7.obratno({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_obratno_29(self):
        modul = 29
        resitev = [1, 15, 10, 22, 6, 5, 25, 11, 13, 3, 8, 17, 9, 27, 2,
                   20, 12, 21, 26, 16, 18, 4, 24, 23, 7, 19, 14, 28]
        z_29 = Zp(modul)
        for i in range(1, modul):
            ans = z_29.obratno(i)
            correct = resitev[i - 1]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_29.obratno({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")


class TestKolicnik(unittest.TestCase):
    def test_kolicnik_3(self):
        modul = 3
        resitev = [
            [0, 0],
            [1, 2],
            [2, 1]
        ]
        z_3 = Zp(modul)
        for i in range(modul):
            for j in range(1, modul):
                ans = z_3.kolicnik(i, j)
                correct = resitev[i][j - 1]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_3.kolicnik({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_kolicnik_7(self):
        modul = 7
        resitev = [
            [0, 0, 0, 0, 0, 0],
            [1, 4, 5, 2, 3, 6],
            [2, 1, 3, 4, 6, 5],
            [3, 5, 1, 6, 2, 4],
            [4, 2, 6, 1, 5, 3],
            [5, 6, 4, 3, 1, 2],
            [6, 3, 2, 5, 4, 1]]
        z_7 = Zp(modul)
        for i in range(modul):
            for j in range(1, modul):
                ans = z_7.kolicnik(i, j)
                correct = resitev[i][j - 1]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_7.kolicnik({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_kolicnik_29(self):
        modul = 29
        resitev = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 15, 10, 22, 6, 5, 25, 11, 13, 3, 8, 17, 9, 27, 2, 20, 12, 21, 26, 16, 18, 4, 24, 23, 7, 19, 14, 28],
            [2, 1, 20, 15, 12, 10, 21, 22, 26, 6, 16, 5, 18, 25, 4, 11, 24, 13, 23, 3, 7, 8, 19, 17, 14, 9, 28, 27],
            [3, 16, 1, 8, 18, 15, 17, 4, 10, 9, 24, 22, 27, 23, 6, 2, 7, 5, 20, 19, 25, 12, 14, 11, 21, 28, 13, 26],
            [4, 2, 11, 1, 24, 20, 13, 15, 23, 12, 3, 10, 7, 21, 8, 22, 19, 26, 17, 6, 14, 16, 9, 5, 28, 18, 27, 25],
            [5, 17, 21, 23, 1, 25, 9, 26, 7, 15, 11, 27, 16, 19, 10, 13, 2, 18, 14, 22, 3, 20, 4, 28, 6, 8, 12, 24],
            [6, 3, 2, 16, 7, 1, 5, 8, 20, 18, 19, 15, 25, 17, 12, 4, 14, 10, 11, 9, 21, 24, 28, 22, 13, 27, 26, 23],
            [7, 18, 12, 9, 13, 6, 1, 19, 4, 21, 27, 3, 5, 15, 14, 24, 26, 2, 8, 25, 10, 28, 23, 16, 20, 17, 11, 22],
            [8, 4, 22, 2, 19, 11, 26, 1, 17, 24, 6, 20, 14, 13, 16, 15, 9, 23, 5, 12, 28, 3, 18, 10, 27, 7, 25, 21],
            [9, 19, 3, 24, 25, 16, 22, 12, 1, 27, 14, 8, 23, 11, 18, 6, 21, 15, 2, 28, 17, 7, 13, 4, 5, 26, 10, 20],
            [10, 5, 13, 17, 2, 21, 18, 23, 14, 1, 22, 25, 3, 9, 20, 26, 4, 7, 28, 15, 6, 11, 8, 27, 12, 16, 24, 19],
            [11, 20, 23, 10, 8, 26, 14, 5, 27, 4, 1, 13, 12, 7, 22, 17, 16, 28, 25, 2, 24, 15, 3, 21, 19, 6, 9, 18],
            [12, 6, 4, 3, 14, 2, 10, 16, 11, 7, 9, 1, 21, 5, 24, 8, 28, 20, 22, 18, 13, 19, 27, 15, 26, 25, 23, 17],
            [13, 21, 14, 25, 20, 7, 6, 27, 24, 10, 17, 18, 1, 3, 26, 28, 11, 12, 19, 5, 2, 23, 22, 9, 4, 15, 8, 16],
            [14, 7, 24, 18, 26, 12, 2, 9, 8, 13, 25, 6, 10, 1, 28, 19, 23, 4, 16, 21, 20, 27, 17, 3, 11, 5, 22, 15],
            [15, 22, 5, 11, 3, 17, 27, 20, 21, 16, 4, 23, 19, 28, 1, 10, 6, 25, 13, 8, 9, 2, 12, 26, 18, 24, 7, 14],
            [16, 8, 15, 4, 9, 22, 23, 2, 5, 19, 12, 11, 28, 26, 3, 1, 18, 17, 10, 24, 27, 6, 7, 20, 25, 14, 21, 13],
            [17, 23, 25, 26, 15, 27, 19, 13, 18, 22, 20, 28, 8, 24, 5, 21, 1, 9, 7, 11, 16, 10, 2, 14, 3, 4, 6, 12],
            [18, 9, 6, 19, 21, 3, 15, 24, 2, 25, 28, 16, 17, 22, 7, 12, 13, 1, 4, 27, 5, 14, 26, 8, 10, 23, 20, 11],
            [19, 24, 16, 12, 27, 8, 11, 6, 15, 28, 7, 4, 26, 20, 9, 3, 25, 22, 1, 14, 23, 18, 21, 2, 17, 13, 5, 10],
            [20, 10, 26, 5, 4, 13, 7, 17, 28, 2, 15, 21, 6, 18, 11, 23, 8, 14, 27, 1, 12, 22, 16, 25, 24, 3, 19, 9],
            [21, 25, 7, 27, 10, 18, 3, 28, 12, 5, 23, 9, 15, 16, 13, 14, 20, 6, 24, 17, 1, 26, 11, 19, 2, 22, 4, 8],
            [22, 11, 17, 20, 16, 23, 28, 10, 25, 8, 2, 26, 24, 14, 15, 5, 3, 27, 21, 4, 19, 1, 6, 13, 9, 12, 18, 7],
            [23, 26, 27, 13, 22, 28, 24, 21, 9, 11, 10, 14, 4, 12, 17, 25, 15, 19, 18, 20, 8, 5, 1, 7, 16, 2, 3, 6],
            [24, 12, 8, 6, 28, 4, 20, 3, 22, 14, 18, 2, 13, 10, 19, 16, 27, 11, 15, 7, 26, 9, 25, 1, 23, 21, 17, 5],
            [25, 27, 18, 28, 5, 9, 16, 14, 6, 17, 26, 19, 22, 8, 21, 7, 10, 3, 12, 23, 15, 13, 20, 24, 1, 11, 2, 4],
            [26, 13, 28, 21, 11, 14, 12, 25, 19, 20, 5, 7, 2, 6, 23, 27, 22, 24, 9, 10, 4, 17, 15, 18, 8, 1, 16, 3],
            [27, 28, 9, 14, 17, 19, 8, 7, 3, 23, 13, 24, 11, 4, 25, 18, 5, 16, 6, 26, 22, 21, 10, 12, 15, 20, 1, 2],
            [28, 14, 19, 7, 23, 24, 4, 18, 16, 26, 21, 12, 20, 2, 27, 9, 17, 8, 3, 13, 11, 25, 5, 6, 22, 10, 15, 1]]
        z_29 = Zp(modul)
        for i in range(modul):
            for j in range(1, modul):
                ans = z_29.kolicnik(i, j)
                correct = resitev[i][j - 1]
                self.assertEqual(ans, correct, msg=f"Napaka pri z_29.kolicnik({i}, {j})\n"
                                                   f"Tvoj odgovor: {ans}, rešitev: {correct}")


class TestPotenca(unittest.TestCase):

    def test_potenca_3(self):
        modul = 3
        resitev = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]
        z_p = Zp(modul)
        for i in range(1, modul):
            for j in range(-10, 11):
                ans = z_p.potenca(i, j)
                correct = resitev[i - 1][j + 10]
                self.assertEqual(ans, correct,
                                 msg=f"Napaka pri Z_3.potenca({i},{j})\nTvoj odgovor: {ans}, rešitev: {correct}")

    def test_potenca_7(self):
        modul = 7
        resitev = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [4, 1, 2, 4, 1, 2, 4, 1, 2, 4, 1, 2, 4, 1, 2, 4, 1, 2, 4, 1, 2],
            [2, 6, 4, 5, 1, 3, 2, 6, 4, 5, 1, 3, 2, 6, 4, 5, 1, 3, 2, 6, 4],
            [2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, 4],
            [4, 6, 2, 3, 1, 5, 4, 6, 2, 3, 1, 5, 4, 6, 2, 3, 1, 5, 4, 6, 2],
            [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1]]
        z_p = Zp(modul)
        for i in range(1, modul):
            for j in range(-10, 11):
                ans = z_p.potenca(i, j)
                correct = resitev[i - 1][j + 10]
                self.assertEqual(ans, correct,
                                 msg=f"Napaka pri Z_7.potenca({i},{j})\nTvoj odgovor: {ans}, rešitev: {correct}")

    def test_potenca_29(self):
        modul = 29
        resitev = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [13, 26, 23, 17, 5, 10, 20, 11, 22, 15, 1, 2, 4, 8, 16, 3, 6, 12, 24, 19, 9],
            [6, 18, 25, 17, 22, 8, 24, 14, 13, 10, 1, 3, 9, 27, 23, 11, 4, 12, 7, 21, 5],
            [24, 9, 7, 28, 25, 13, 23, 5, 20, 22, 1, 4, 16, 6, 24, 9, 7, 28, 25, 13, 23],
            [16, 22, 23, 28, 24, 4, 20, 13, 7, 6, 1, 5, 25, 9, 16, 22, 23, 28, 24, 4, 20],
            [20, 4, 24, 28, 23, 22, 16, 9, 25, 5, 1, 6, 7, 13, 20, 4, 24, 28, 23, 22, 16],
            [23, 16, 25, 1, 7, 20, 24, 23, 16, 25, 1, 7, 20, 24, 23, 16, 25, 1, 7, 20, 24],
            [22, 2, 16, 12, 9, 14, 25, 26, 5, 11, 1, 8, 6, 19, 7, 27, 13, 17, 20, 15, 4],
            [7, 5, 16, 28, 20, 6, 25, 22, 24, 13, 1, 9, 23, 4, 7, 5, 16, 28, 20, 6, 25],
            [5, 21, 7, 12, 4, 11, 23, 27, 9, 3, 1, 10, 13, 14, 24, 8, 22, 17, 25, 18, 6],
            [4, 15, 20, 17, 13, 27, 7, 19, 6, 8, 1, 11, 5, 26, 25, 14, 9, 12, 16, 2, 22],
            [28, 17, 1, 12, 28, 17, 1, 12, 28, 17, 1, 12, 28, 17, 1, 12, 28, 17, 1, 12, 28],
            [25, 6, 20, 28, 16, 5, 7, 4, 23, 9, 1, 13, 24, 22, 25, 6, 20, 28, 16, 5, 7],
            [9, 10, 24, 17, 6, 26, 16, 21, 4, 27, 1, 14, 22, 18, 20, 19, 5, 12, 23, 3, 13],
            [9, 19, 24, 12, 6, 3, 16, 8, 4, 2, 1, 15, 22, 11, 20, 10, 5, 17, 23, 26, 13],
            [25, 23, 20, 1, 16, 24, 7, 25, 23, 20, 1, 16, 24, 7, 25, 23, 20, 1, 16, 24, 7],
            [28, 12, 1, 17, 28, 12, 1, 17, 28, 12, 1, 17, 28, 12, 1, 17, 28, 12, 1, 17, 28],
            [4, 14, 20, 12, 13, 2, 7, 10, 6, 21, 1, 18, 5, 3, 25, 15, 9, 17, 16, 27, 22],
            [5, 8, 7, 17, 4, 18, 23, 2, 9, 26, 1, 19, 13, 15, 24, 21, 22, 12, 25, 11, 6],
            [7, 24, 16, 1, 20, 23, 25, 7, 24, 16, 1, 20, 23, 25, 7, 24, 16, 1, 20, 23, 25],
            [22, 27, 16, 17, 9, 15, 25, 3, 5, 18, 1, 21, 6, 10, 7, 2, 13, 12, 20, 14, 4],
            [23, 13, 25, 28, 7, 9, 24, 6, 16, 4, 1, 22, 20, 5, 23, 13, 25, 28, 7, 9, 24],
            [20, 25, 24, 1, 23, 7, 16, 20, 25, 24, 1, 23, 7, 16, 20, 25, 24, 1, 23, 7, 16],
            [16, 7, 23, 1, 24, 25, 20, 16, 7, 23, 1, 24, 25, 20, 16, 7, 23, 1, 24, 25, 20],
            [24, 20, 7, 1, 25, 16, 23, 24, 20, 7, 1, 25, 16, 23, 24, 20, 7, 1, 25, 16, 23],
            [6, 11, 25, 12, 22, 21, 24, 15, 13, 19, 1, 26, 9, 2, 23, 18, 4, 17, 7, 8, 5],
            [13, 3, 23, 12, 5, 19, 20, 18, 22, 14, 1, 27, 4, 21, 16, 26, 6, 17, 24, 10, 9],
            [1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1]]
        z_p = Zp(modul)
        for i in range(1, modul):
            for j in range(-10, 11):
                ans = z_p.potenca(i, j)
                correct = resitev[i - 1][j + 10]
                self.assertEqual(ans, correct,
                                 msg=f"Napaka pri Z_29.potenca({i},{j})\nTvoj odgovor: {ans}, rešitev: {correct}")


class TestSteviloKvadratnihKorenov(unittest.TestCase):

    def test_kvadratni_koreni_3(self):
        modul = 3
        resitev = [1, 2, 0]
        z_3 = Zp(modul)
        for i in range(modul):
            ans = z_3.stevilo_kvadratnih_korenov(i)
            correct = resitev[i]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_3.stevilo_kvadratnih_korenov({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_kvadratni_koreni_7(self):
        modul = 7
        resitev = [1, 2, 2, 0, 2, 0, 0]
        z_7 = Zp(modul)
        for i in range(modul):
            ans = z_7.stevilo_kvadratnih_korenov(i)
            correct = resitev[i]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_7.stevilo_kvadratnih_korenov({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_kvadratni_koreni_29(self):
        modul = 29
        resitev = [1, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 0, 2]
        z_29 = Zp(modul)
        for i in range(modul):
            ans = z_29.stevilo_kvadratnih_korenov(i)
            correct = resitev[i]
            self.assertEqual(ans, correct, msg=f"Napaka pri z_29.stevilo_kvadratnih_korenov({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")


class TestJeMultiplikativniGenerator(unittest.TestCase):

    def test_multiplikativni_generator_3(self):
        modul = 3
        multiplicative_generators = {2}
        z_3 = Zp(modul)
        for i in range(modul):
            ans = z_3.je_multiplikativni_generator(i)
            correct = i in multiplicative_generators
            self.assertEqual(ans, correct, msg=f"Napaka pri z_3.je_multiplikativni_generator({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_multiplikativni_generator_7(self):
        modul = 7
        multiplicative_generators = {3, 5}
        z_7 = Zp(modul)
        for i in range(modul):
            ans = z_7.je_multiplikativni_generator(i)
            correct = i in multiplicative_generators
            self.assertEqual(ans, correct, msg=f"Napaka pri z_7.je_multiplikativni_generator({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")

    def test_multiplikativni_generator_29(self):
        modul = 29
        multiplicative_generators = {2, 3, 8, 10, 11, 14, 15, 18, 19, 21, 26, 27}
        z_29 = Zp(modul)
        for i in range(modul):
            ans = z_29.je_multiplikativni_generator(i)
            correct = i in multiplicative_generators
            self.assertEqual(ans, correct, msg=f"Napaka pri z_29.je_multiplikativni_generator({i})\n"
                                               f"Tvoj odgovor: {ans}, rešitev: {correct}")


if __name__ == "__main__":
    unittest.main()
