var mysql = require('mysql');
var pool = mysql.createPool({
  connectionLimit : 10,
  host            : 'classmysql.engr.oregonstate.edu',
  user            : 'cs290_yangwo',
  password        : '3549',
  database        : 'cs290_yangwo'
});

module.exports.pool = pool
