#customize.js
#####测试环境
<pre>
windows7
centeros6.5
node -v v0.12.2
</pre>

在路由配置入口<pre>var customize = require('./customize');
router.post('/dao', function(req, res, next) {
     return customize.do(req.body,res);
});
</pre>

说明<pre>1. 入口基于express，实现依赖于nodejs的原生包
2. 未能解决编码问题（默认utf8）
3. 未能解决数据库问题（需要依赖外部包）
4. 未能解决文件上传问题（caidao本身原因）
</pre>


