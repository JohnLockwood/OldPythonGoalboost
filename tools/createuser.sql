use apitest
db.createUser(
  {
    user: "apitestUser",
    pwd: "asf$$95yXpiorE",
    roles: [ { role: "userAdmin", db: "apitest" } ]
  }
)