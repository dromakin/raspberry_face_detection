from picamera import PiCamera
from time import sleep

# Создаём объект для работы с камерой
camera = PiCamera()

# Запускаем предпросмотр сигнала с камеры на экране поверх всех окон
camera.start_preview()

# Пауза программы на 10 секунд
sleep(10)

# Выключаем предпросмотр
camera.stop_preview()