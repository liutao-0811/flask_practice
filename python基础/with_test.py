class Testwith():
    def __enter__(self):
        print("run")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

with Testwith():
    print("is running")