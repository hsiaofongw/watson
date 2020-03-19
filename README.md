# Modelling WebSite's meta-data -- an Object-Oriented Approach

## Abstract 

Nowadays it's more easy and cheap, to build, to maintain, and to publish a WebSite to the Internet, since doing this makes a lot of fun, and people who doing this can learning so much knowledge about computer science and network from this, there are already a huge number of websites people have already built and published on the Internet. We propose a new (not very new actually) perspective to model and monitor arbitary website by simply treating a website as an abstract Object just like treating a project like a Object (see POM). There's nothing new but new perspective in this article.

## Introduction

A WebSite is simply (if you like simplicity) can be treated as a bulk of web pages, each of them contains meta-data and data, each of them (i.e. each page) showing text, pictures, musics, videos, links or whatever when be faced at a browser. A language called Hyper Text Markup Language (H.T.M.L.) are popularly used to encode data and information what people wanna express on a web page, you may consider a web page is nothing but a file that store HTML codes to convey informations.

Generally speaking, Our approch is just to, simply, cut a special snippet of a web page (which are call the head tag) and using its content to initialize an `WebSiteMetaDataObject` them everything will just begin since `this`, this  `webSiteMetaDataObject`.

A `WebSiteMetaDataObject` can be `Comparable`, and espcially can compare with another `WebsiteMetaDataObject` against their age: to know which one is newer. A `WebSiteMetaDataObject` is also, is also sometimes, uh, `Inspectable`, that means, given A `WebSiteMetaDataObject` one may be able to get its title or author's name for example via `getTitle(): String` or `getAuthorName(): String`.

