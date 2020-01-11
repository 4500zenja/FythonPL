import Main
string = ""
def ReadBlock (s = "", ind = " "*8, t = False):
        while True:
                s = Main.Interact.Input("   >>> ")
                if s.startswith("if") or s.startswith("elif") or s.startswith("else") or s.startswith("for") or s.startswith("while") or s.startswith("def") or s.startswith("class"):
                        pass
                elif s != "ESC":
                        exec(s)
                else:
                        break
ReadBlock()
