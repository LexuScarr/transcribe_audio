import whisper

def speech_recognition(model='base'):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe("skillet-monster.mp3")
    # with open(f'transcription_{model}.txt', 'w', encoding='utf-8') as file:
    #     file.write(result['text'])

    with open(f'transcription_{model}.txt', 'w', encoding='utf-8') as file:
        for i, seg in enumerate(result['segments']):
            file.write(f"{i+1} - {seg['text']}\n")

def main():
    models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}

    for k, v in models.items():
        print(f'{k}:{v}')

    model = int(input('Выберите модель от 1 до 5: '))

    if model not in models.keys():
        raise KeyError(f'Модели {model} нет в списке!')

    print('Запущен процесс транскрибации')
    speech_recognition(model=models[model])


if __name__ == '__main__':
    main()
