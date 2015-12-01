#ES Introduction

###What is ES?

1.	Elasticsearch is a tool for querying written words. It can perform some other nifty tasks, but at its core it’s made for wading through text, returning text similar to a given query and/or statistical analyses of a corpus of text.

2.	More specifically, elasticsearch is a standalone database server, written in Java, that takes data in and stores it in a sophisticated format optimized for language based searches. Working with it is convenient as its main protocol is implemented with HTTP/JSON. Elasticsearch is also easily scalable, supporting clustering and leader election out of the box.

Whether it’s searching a database of retail products by description, finding similar text in a body of crawled web pages, or searching through posts on a blog, elasticsearch is a fantastic choice. When facing the task of cutting through the semi-structured muck that is natural language, Elasticsearch is an excellent tool.

###Use case
1.	Searching a large number of product descriptions for the best match for a specific phrase (say “chef’s knife”) and returning the best results
2.	Given the previous example, breaking down the various departments where “chef’s knife” appears (see Faceting later in this book)
3.	Searching text for words that sound like “season”
4.	Auto-completing a search box based on partially typed words based on previously issued searches while accounting for mis-spellings
5.	Storing a large quantity of semi-structured (JSON) data in a distributed fashion, with a specified level of redundancy across a cluster of machines