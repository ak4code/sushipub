const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? ''
        : 'http://localhost:8080/',
    css: {
        extract: true
    },
    configureWebpack: {
        plugins: [
            new BundleTracker({filename: process.env.NODE_ENV === 'production' ? './webpack-prod-stats.json' : './webpack-stats.json'})
        ]
    },
    runtimeCompiler: true
}