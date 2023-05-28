# transcribe_audio
transcribe audio openai-whisper
Whisper - это универсальная модель распознавания речи от OpenAI. Она обучена на большом наборе разнообразных аудио и является многозадачной моделью, которая может выполнять многоязычное распознавание речи, перевод речи и идентификацию языка.

Данный код использует библиотеку whisper для распознавания речи. Разберем каждую часть кода подробнее:
Здесь происходит импорт библиотеки whisper, которая предоставляет функции для работы с моделью распознавания речи.

    import whisper

В этой функции speech_recognition происходит распознавание речи с использованием модели, указанной в параметре model. Функция загружает модель с помощью whisper.load_model(model). Затем происходит вызов метода transcribe, где передается файл с аудиозаписью "skillet-monster.mp3" для распознавания речи. Результат сохраняется в переменную result. 
Затем, с помощью конструкции with open, создается файл с именем transcription_{model}.txt для сохранения результатов распознавания. Далее, в цикле for происходит перебор итерируемого объекта result['segments'], где каждый сегмент речи сохраняется в файл в формате номер_сегмента - текст_сегмента.

    def speech_recognition(model='base'):
        speech_model = whisper.load_model(model)
        result = speech_model.transcribe("skillet-monster.mp3")
        # with open(f'transcription_{model}.txt', 'w', encoding='utf-8') as file:
        #     file.write(result['text'])
        with open(f'transcription_{model}.txt', 'w', encoding='utf-8') as file:
            for i, seg in enumerate(result['segments']):
                file.write(f"{i+1} - {seg['text']}\n")

В функции main() создается словарь models, который сопоставляет номер модели с именем модели. Затем происходит вывод на экран всех доступных моделей с их номерами.
После этого пользователю предлагается выбрать модель, указав номер от 1 до 5 с помощью функции input(). Если указанный номер модели не существует в словаре models, выбрасывается исключение KeyError.
Затем выводится сообщение о запуске процесса транскрибации и вызывается функция speech_recognition с указанной моделью.

    def main():
        models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}

        for k, v in models.items():
            print(f'{k}:{v}')

        model = int(input('Выберите модель от 1 до 5: '))

        if model not in models.keys():
            raise KeyError(f'Модели {model} нет в списке!')

        print('Запущен процесс транскрибации')
        speech_recognition(model=models[model])

для работы нужно установить pip install openai-whisper 
Руководства:
https://pypi.org/project/openai-whisper/
https://analyzingalpha.com/openai-whisper-python-tutorial 
Так же нужно скачать FFmpeg "https://ffmpeg.org/download.html"
