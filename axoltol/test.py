import axoltol
import time

class Test:
    def window():
        axoltol.init()
        window = axoltol.Window()
        time.sleep(1)
        axoltol.quit()

    def renderer():
        axoltol.init()
        window = axoltol.Window()
        renderer = axoltol.Renderer(window)
        renderer.setDrawColor(255, 255, 255)
        renderer.clear()
        renderer.present()
        time.sleep(1)
        axoltol.quit()


if __name__ == "__main__":
    Test.window()
    print("Window works!")
    Test.renderer()
    print("Renderer works!")
    print("Everything successful!")
