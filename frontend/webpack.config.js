const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebPackPlugin = require('html-webpack-plugin');

module.exports = {

    entry: ['./src/js/Index.js', '@babel/polyfill'],

    output: {
        path: path.resolve(__dirname, 'dist/js'),
        filename: 'bundle.js'
    },

    plugins: [
        new MiniCssExtractPlugin( {filename: '../css/styles.css'} ),
        new HtmlWebPackPlugin({
            template: "src/index.html",
            filename: "../../index.html"
        })
    ],

    module: {
        rules: [
            {   // javascript 파일 규칙
                test: /\.(js|jsx)$/,
                include: [
                    path.resolve(__dirname, 'src/js')
                ],
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react'],
                        plugins: ['@babel/plugin-proposal-class-properties']
                    }
                }
            },
            {   // html 파일 규칙
                test: /\.html$/,
                use: {
                    loader: 'html-loader',
                    options: {minimize: true}
                }
            },
            {   // css 파일 규칙
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader"
                ]
            }
        ]
    },

    devtool: 'source-map',
    mode: 'development'

}