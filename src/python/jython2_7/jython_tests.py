import types
import unittest


class JythonTests(unittest.TestCase):

    def test_identifyFunction_callableAndFunctionType(self):
        def func():
            pass

        self.assertTrue(callable(func))
        self.assertTrue(isinstance(func, types.FunctionType))
        pass

    def test_identifyFunction_Or_Method(self):
        class Work:
            def show(self):
                pass

            pass

        workInstance = Work()

        self.assertFalse(isinstance(Work.show, types.FunctionType))
        self.assertTrue(isinstance(Work.show, types.MethodType))
        self.assertTrue(callable(Work.show))

        self.assertFalse(isinstance(workInstance.show, types.FunctionType))
        self.assertTrue(isinstance(workInstance.show, types.MethodType))
        self.assertTrue(callable(workInstance.show))
        pass

    def test_class_IsCallableNotFunctionType(self):
        class NotFuncClass:
            def __init__(self):
                pass

        self.assertTrue(callable(NotFuncClass))
        self.assertFalse(isinstance(NotFuncClass, types.FunctionType))
        pass

    def test_classInfo_howToGetClassInfo(self):
        from java.lang import Exception as JException
        try:
            raise JException()
        except JException, jE:
            print jE.__class__.__name__
            self.assertEqual(jE.__class__.__name__, u"Exception")
            pass
        pass

    def test_classInfo_Mock(self):
        class Demo(object):

            def __init__(self):
                self.demoName = u"A"
                pass

        instance = Demo()
        MockClass = type("Demo", (Demo, object,), {"demoName": u"A"})
        mockInstance = MockClass()

        print instance
        print mockInstance
        self.assertEqual(instance.__class__.__module__, mockInstance.__class__.__module__)

        self.assertEqual(instance.demoName, mockInstance.demoName)

        print type(instance)
        print type(mockInstance)

        self.assertTrue(isinstance(instance, Demo))
        self.assertTrue(isinstance(mockInstance, Demo))
        pass

    def test_none_NoneIsNotTypesButNoneType(self):
        noneObj = None

        self.assertTrue(isinstance(noneObj, types.NoneType))
        self.assertFalse(isinstance(noneObj, types.ClassType))
        pass
