import unittest
import DBTree

class DBNodeTests(unittest.TestCase):
    def setUp(self):
        self.rootNode = DBTree.DBNode(None, None)
        newNode = DBTree.DBNode("test")
        self.rootNode.add(newNode)

    def testAdd(self):
        self.assertIn("test", self.rootNode.children)
    
    def testSearchChildren(self):
        result = self.rootNode.searchChildren("test")
        self.assertEqual(result.item, "test")
        self.assertEqual(result.count, 1)

        result = self.rootNode.searchChildren("somethingElse")
        self.assertEqual(result, None)

class DBTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = DBTree.DBTree()

    def testAddOneTransaction(self):
        transaction = ['a', 'b', 'c']
        self.tree.add(transaction)

        self.assertIn('a', self.tree.root.children)
        self.assertIn('b', self.tree.root.children['a'].children)
        self.assertIn('c', self.tree.root.children['a'].children['b'].children)
    
    def testAddIndependentTransactions(self):
        t1 = ['a', 'b']
        t2 = ['d', 'e']
        self.tree.add(t1)
        self.tree.add(t2)

        # two direct children off the root node
        self.assertIn('a', self.tree.root.children)
        self.assertIn('d', self.tree.root.children)

        # each of them have one child
        self.assertIn('b', self.tree.root.children['a'].children)
        self.assertIn('e', self.tree.root.children['d'].children)

    def testAddCommonPrefixes(self):
        t1 = ['a', 'b']
        t2 = ['a', 'e']
        self.tree.add(t1)
        self.tree.add(t2)

        self.assertIn('a', self.tree.root.children)
        self.assertEqual(self.tree.root.children['a'].count, 2)

        self.assertIn('b', self.tree.root.children['a'].children)
        self.assertEqual(self.tree.root.children['a'].children['b'].count, 1)

        self.assertIn('e', self.tree.root.children['a'].children)
        self.assertEqual(self.tree.root.children['a'].children['e'].count, 1)

    def testGetPaths(self):
        tdb = [
            ['a','c','d'],
            ['b','c','e'],
            ['a','b','c','e'],
            ['b','e']
        ]

        self.tree.buildTree(tdb)
        self.assertIn(['a','c','d'], DBTree.getPaths(self.tree))
        self.assertIn(['b','c','e'], DBTree.getPaths(self.tree))
        self.assertIn(['a','b','c','e'], DBTree.getPaths(self.tree))
        self.assertIn(['b','e'], DBTree.getPaths(self.tree))
