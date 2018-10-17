import unittest
import gcd


class TestGCD(unittest.TestCase):

    def test_gsd_in_param(self):
        self.assertEqual(gcd.gcd(0, 7), 7)
        self.assertEqual(gcd.gcd(7, 0), 7)
        self.assertEqual(gcd.gcd(7, 7), 7)
        self.assertEqual(gcd.gcd(1, 8), 1)
        self.assertEqual(gcd.gcd(4, 6), 2)
        self.assertEqual(gcd.gcd(10, 15), 5)
        self.assertEqual(gcd.gcd(15, 10), 5)
        self.assertEqual(gcd.gcd(5, 25), 5)
        self.assertEqual(gcd.gcd(15, 45), 15)

    def test_gsd_change_of_positions(self):
        for n in range(20):
            for m in range(20):
                self.assertEqual(gcd.gcd(n, m), gcd.gcd(m, n))

    def test_out_int(self):
        for n in range(20):
            for m in range(20):
                result = gcd.gcd(n, m)
                if result!=0:
                    result = result/int(result)
                    self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()


'''
Описание модуля unittest:
    https://pythonworld.ru/moduli/modul-unittest.html

Специальные функци:
    def setUp(self):
        # Код настройки - перед запуском тестов
        pass

    def tearDown(self):
        # Код после выполнения тестов
        pass

Пропуск тестов:
    @unittest.skip(reason) - пропустить тест. reason описывает причину пропуска.
    @unittest.skipIf(condition, reason) - пропустить тест, если condition истинно.
    @unittest.skipUnless(condition, reason) - пропустить тест, если condition ложно.
    @unittest.expectedFailure - пометить тест как ожидаемая ошибка.

Функции для проверок:
    assertEqual(a, b) — a == b
    assertNotEqual(a, b) — a != b
    assertTrue(x) — bool(x) is True
    assertFalse(x) — bool(x) is False
    assertIs(a, b) — a is b
    assertIsNot(a, b) — a is not b
    assertIsNone(x) — x is None
    assertIsNotNone(x) — x is not None
    assertIn(a, b) — a in b
    assertNotIn(a, b) — a not in b
    assertIsInstance(a, b) — isinstance(a, b)
    assertNotIsInstance(a, b) — not isinstance(a, b)
    assertRaises(exc, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc
    assertRaisesRegex(exc, r, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc и сообщение соответствует регулярному выражению r
    assertWarns(warn, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение
    assertWarnsRegex(warn, r, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение и сообщение соответствует регулярному выражению r
    assertAlmostEqual(a, b) — round(a-b, 7) == 0
    assertNotAlmostEqual(a, b) — round(a-b, 7) != 0
    assertGreater(a, b) — a > b
    assertGreaterEqual(a, b) — a >= b
    assertLess(a, b) — a < b
    assertLessEqual(a, b) — a <= b
    assertRegex(s, r) — r.search(s)
    assertNotRegex(s, r) — not r.search(s)
    assertCountEqual(a, b) — a и b содержат те же элементы в одинаковых количествах, но порядок не важен
'''