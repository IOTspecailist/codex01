import os


def main():
    message_file = os.path.join(os.path.dirname(__file__), 'message.txt')
    try:
        with open(message_file, 'r', encoding='utf-8') as f:
            message = f.read().strip()
            if not message:
                message = 'this is dec branch'
    except FileNotFoundError:
        message = 'this is dec branch'
    print(message)

if __name__ == '__main__':
    main()
