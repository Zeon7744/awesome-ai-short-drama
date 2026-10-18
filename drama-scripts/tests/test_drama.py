import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import drama_engine

class TestEngine(unittest.TestCase):
    def test_enums(self):
        self.assertEqual(drama_engine.DramaPlatform.DOUYIN.value, "douyin")
        self.assertEqual(drama_engine.DramaGenre.ROMANCE.value, "romance")

    def test_character_dict(self):
        c = drama_engine.Character(name="测试", role="protagonist", description="主角", age=30)
        d = c.to_dict()
        self.assertEqual(d["name"], "测试")
        self.assertEqual(d["role"], "protagonist")

if __name__ == "__main__":
    unittest.main()
