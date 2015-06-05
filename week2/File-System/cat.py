def main():
    filename = "file.txt"
    file = open(filename, "r")
    content = file.read()
    print(content)

    file.close()

if __name__ == '__main__':
    main()
