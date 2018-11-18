class worker:
    name = "IT"

    @staticmethod
    def learn():
        print("CV")

    def work(self):
        print("bill")


def main():
    Yury = worker()
    Yury.work()
    Yury.learn()


if __name__ == '__main__':
    worker.learn()
    print(worker.name)
    main()
    worker().work()
