<code>
1. 入口基于express，实现依赖于nodejs的原生包
2. 未能解决编码问题
3. 未能解决数据库问题
4. 未能解决文件上传问题
</code>

在路由配置入口
<code>
var customize = require('./customize');
router.post('/dao', function(req, res, next) {
     return customize.do(req.body,res);
});
</code>

