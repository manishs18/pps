import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Calc:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        logging.info("Constr Created.")

    def add(self):
        logging.info("Addition successful.")
        return self.x+self.y

    def div(self):
        try:
            logging.debug("Division method was called")
            r = self.x/self.y
        except ZeroDivisionError as e:
            logging.error(f"Error: {e}")
            print("Error: ",e)
        else:
            logging.info("Division successful.")
            return r

if __name__ == "__main__":
    c1 = Calc(10,20)

    print(c1.add())
    print(c1.div())

    c2 = Calc(10,0)

    print(c2.add())
    print(c2.div())

