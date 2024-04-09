from matplotlib import pyplot as plt


prefix = "CIFAR10_VGG/output_"
task = ["1a", "1b", "1c", "2a", "2b", "2c", "2d"]
for t in task:
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    file = prefix + t + ".txt"
    y = []
    x = []
    testx = []
    testy = []
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            a = line.strip().split(" ")
            if len(a[-1]) == 0:
                continue
            if a[-1][0] != '(':
                x.append(int(a[2]))
                y.append(float(a[-1]))
            else:
                testx.append(x[-1])
                testy.append(float(a[-1].strip('()%'))/100)

        ax2.set_ylim(0, 1)
        ax1.plot(x, y, 'o', label="training loss")
        ax2.plot(testx, testy, '*', color="orange", label="test accuracy")
        ax1.set_xlabel("Epoch")
        ax1.set_ylabel("Train loss")
        ax2.set_ylabel("Test accuracy")
        ax1.legend(loc="upper left")
        ax2.legend(loc="upper right")
        plt.show()
