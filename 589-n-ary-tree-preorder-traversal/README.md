<h2><a href="https://leetcode.com/problems/n-ary-tree-preorder-traversal/">589. N-ary Tree Preorder Traversal</a></h2><h3>Easy</h3><hr><div><p><font _mstmutation="1" _msthash="489671" _msttexthash="3526354">Given the  of an n-ary tree, return <em _mstmutation="1">the preorder traversal of its nodes' values</em>.</font><code>root</code></p>

<p _msthash="489788" _msttexthash="11503934">Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)</p>

<p>&nbsp;</p>
<p><strong _msthash="490022" _msttexthash="114439">Example 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;"></p>

<pre><strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [1,3,5,6,2,4]
</pre>

<p><strong _msthash="490373" _msttexthash="114621">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;"></p>

<pre><strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
</pre>

<p>&nbsp;</p>
<p><strong _msthash="519662" _msttexthash="199901">Constraints:</strong></p>

<ul>
	<li><font _mstmutation="1" _msthash="745030" _msttexthash="1309607">The number of nodes in the tree is in the range .</font><code>[0, 10<sup>4</sup>]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><font _mstmutation="1" _msthash="745290" _msttexthash="1640353">The height of the n-ary tree is less than or equal to .</font><code>1000</code></li>
</ul>

<p>&nbsp;</p>
<p _msthash="520052" _msttexthash="3029208"><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>
</div>