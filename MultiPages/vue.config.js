var  path = require( 'path' )
module.exports = {
  outputDir: '../Project/dist',
    pages: {
      index: {
        // page 的入口
        entry: './src/pages/Homepage/main.js',
        // 模板来源
        template: './public/index.html',
        // 在 dist/index.html 的输出
        filename: 'index.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: '智慧电池-电池智能管理',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'index']
      },
      batterymanage: {
        // page 的入口
        entry: './src/pages/BatteryManage/analysis/BatteryManagemain.js',
        // 模板来源
        template: './public/batterymanage.html',
        // 在 dist/index.html 的输出
        filename: 'batterymanage.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: 'Battery Manage Page',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'batterymanage']
      },
      casecentre: {
        // page 的入口
        entry: './src/pages/CaseCentre/CaseCentremain.js',
        // 模板来源
        template: './public/casecentre.html',
        // 在 dist/index.html 的输出
        filename: 'casecentre.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: 'Case Centre Page',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'casecentre']
      },
      news: {
        // page 的入口
        entry: './src/pages/News/Newsmain.js',
        // 模板来源
        template: './public/news.html',
        // 在 dist/index.html 的输出
        filename: 'news.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: 'News Page',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'news']
      },
      about: {
        // page 的入口
        entry: './src/pages/About/Aboutmain.js',
        // 模板来源
        template: './public/about.html',
        // 在 dist/index.html 的输出
        filename: 'about.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: '关于我们-电池智能管理',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'about']
      },
      // 当使用只有入口的字符串格式时，
      // 模板会被推导为 `public/subpage.html`
      // 并且如果找不到的话，就回退到 `public/index.html`。
      // 输出文件名会被推导为 `subpage.html`。
      // subpage: 'src/subpage/main.js'
      
    },
  assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:5000/'
  }
}