from day02_1 import prog, input

if __name__ == '__main__':
    def test():
        for noun in range(100):
            for verb in range(100):
                if prog(input, noun=noun, verb=verb)[0] == 19690720:
                    return (noun, verb)

    noun, verb = test()

    print(noun*100 + verb)
