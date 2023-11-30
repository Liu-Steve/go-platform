# go-platform

这是武汉大学计算机学院2020级大型课程软件设计课程的小组项目，围棋对弈平台

项目网址 [dragondj.space](https://dragondj.space)

本项目 Github 仓库地址 [go-platform](https://github.com/Liu-Steve/go-platform)

本项目前端 Github 仓库地址 [go-platform-ui](https://github.com/Liu-Steve/go-platform-ui)

本项目后端 Github 仓库地址 [go-platform-server](https://github.com/Liu-Steve/go-platform-server)

## 项目报告

第一轮迭代 [阶段报告](./阶段报告1.md)

第二轮迭代 [阶段报告](./阶段报告2.md)

第三轮迭代 [阶段报告](./阶段报告3.md)

最终报告文档 [最终报告](./武汉大学计算机学院课程设计报告-围棋平台-v0.3.doc)

最终报告PPT [PPT](./围棋平台-最终汇报.pptx)

## 本项目使用的开发框架

前端使用 Vue3 与 Element Plus 框架开发

后端使用 Spring Boot 与 JPA 框架开发

部署时使用 Maven 打包为 Docker 镜像

## 运维脚本介绍

[部署脚本 new-go-server](./script/new-go-server.py) 在 Maven 打包 go-server 镜像完成后运行本脚本，即正常在本机运行起项目

[部署脚本 new-katago](./script/new-katago.py) 在 Maven 打包 katago 镜像完成后运行本脚本，即正常在本机运行起项目

[静态资源更新脚本 copy-static](./script/copy-static.py) 在 ui
项目发生更新，导致 `npm run build` 打包产物 dist 文件夹发生变化后，运行本脚本即可重新打包并更新 server 项目的静态文件
