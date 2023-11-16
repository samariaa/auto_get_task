import keyboard
import pyautogui
from playsound import playsound

pause = ('Нажми CapsLock чтобы начать поиск!')
print(pause)
while True:
    if keyboard.is_pressed('CapsLock'):
        while True:
            try:
                result = pyautogui.locateOnScreen('get_button_black.png', grayscale=False, confidence=0.8)
                print('ТАСК НЕ НАЙДЕН')  # наличие кнопки, значит таск не найден
                pyautogui.click(result)
            except pyautogui.ImageNotFoundException:
                print('ТАСК НАЙДЕН(или кнопка поиска пропала с экрана)')  # когда нопка пропадет, значит нашли таск
                playsound('task.mp3')
                print(pause)
                break