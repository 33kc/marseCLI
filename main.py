import argparse
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="render a equation")
    parser.add_argument("-eq", "--equation", type=str, required=True, help="Equation to render")
    args = parser.parse_args()

    equation = args.equation
    plt.figure(figsize=(6, 2))
    plt.text(0.5, 0.5, f"${equation}$", fontsize=20, ha="center", va="center")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
