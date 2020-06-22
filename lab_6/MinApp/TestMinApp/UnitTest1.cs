using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

using MinApp;

namespace TestMinApp
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMin()
        {
            int min;
            min = Program.Min(3, 4, 5);
            Assert.AreEqual(3, min);
        }
    }
}