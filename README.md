# Personal Blogging Platform API

> Image of project
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](design-system.png)

This is a `RESTful API` that would power a personal blog.

**Functions:**
- Return list of articles.
- Return single article.
- Create new article.
- Delete single article, by the `ID`.
- Update single article, using specify `ID`.

**Tecnologie:**
- MySql
- Python for version 1 (FastAPI)
- Python for version 2 (Flask) -- **review** 
- Golang for version 1.1(learn golang with projects)
- Postman


**Design database**
Construction model of database:
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](design-database.png)

**JSON**

1.Return element in json.dumps(<data>)
2. Next is tranform in json with json.loads(<data>)