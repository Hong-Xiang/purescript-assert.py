def assert_(message):
    def succ(success):
        def ap():
            if not success:
                raise Exception(message)

        return ap

    return succ


globals()["assert"] = assert_


def checkThrows(fn):
    def ap():
        try:
            fn()
        except Exception:
            return True
        raise Exception("Threw something other than an Error")

    return ap

