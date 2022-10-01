<h2><a href="https://leetcode.com/problems/n-ary-tree-postorder-traversal/">590. N-ary Tree Postorder Traversal</a></h2><h3>Easy</h3><hr><div><p><font _mstmutation="1" _msthash="4660643" _msttexthash="3637452">Given the  of an n-ary tree, return <em _mstmutation="1">the postorder traversal of its nodes' values</em>.</font><code>root</code></p>

<p _msthash="4660760" _msttexthash="11503934">Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)</p>

<p>&nbsp;</p>
<p><strong _msthash="4660994" _msttexthash="114439">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;">
<pre><strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [5,6,3,2,4,1]
</pre>

<p><strong _msthash="4661462" _msttexthash="114621">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;">
<pre><strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
</pre>

<p>&nbsp;</p>
<p><strong _msthash="4759027" _msttexthash="199901">Constraints:</strong></p>

<ul>
	<li><font _mstmutation="1" _msthash="5393349" _msttexthash="1309607">The number of nodes in the tree is in the range .</font><code>[0, 10<sup>4</sup>]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><font _mstmutation="1" _msthash="5393609" _msttexthash="1640353">The height of the n-ary tree is less than or equal to .</font><code>1000</code></li>
</ul>

<p>&nbsp;</p>
<p _msthash="4759417" _msttexthash="3029208"><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>
</div>