def main():
    try:
        with open('message.txt', 'r', encoding='utf-8') as f:
            message = f.read().strip()
            if not message:
                message = 'this is dec branch'
    except FileNotFoundError:
        message = 'this is dec branch'
    print(message)

if __name__ == '__main__':
    main()
