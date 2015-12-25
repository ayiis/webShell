## customize.js
##### 测试环境
````javascripts
windows7
centeros6.5
node -v v0.12.2
````

##### 在路由配置入口
````javascripts
var customize = require('./customize');
router.post('/dao', function(req, res, next) {
     return customize.do(req.body,res);
});
````

##### 说明
````javascripts
1. 入口基于express，实现依赖于nodejs的原生包
2. 未能解决编码问题（默认utf8）
3. 未能解决数据库问题（需要依赖外部包）
4. 未能解决文件上传问题（caidao本身原因）
````

#### 2015-12-25 Update

1. 解决编码问题（使用utf8）
