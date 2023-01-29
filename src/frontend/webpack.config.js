const webpack = require("webpack");
const ExtractCSSChunksPlugin = require("extract-css-chunks-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const CopyPlugin = require("copy-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const OptimizeCssAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

const path = require("path");

const config = {
  entry: {
    base: "./src/base.js",
  },
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "[name].js",
    chunkFilename: "[id].[chunkhash].js"
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          "style-loader",
          {
            loader: ExtractCSSChunksPlugin.loader,
            options: {
              hot: true,
              reloadAll: true
            }
          },
          "css-loader",
          "sass-loader"
        ]
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
        include: /\.module\.css$/
      },
      {
        test: /\.woff(2)?(\?v=\d+\.\d+\.\d+)?$/,
        loader:
          "url-loader?limit=10000&mimetype=application/font-woff&name=fonts/[name].[ext]&publicPath=../"
      },
      {
        test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
        loader:
          "url-loader?limit=10000&mimetype=application/octet-stream&name=fonts/[name].[ext]&publicPath=../"
      },
      {
        test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
        loader: "file-loader?name=fonts/[name].[ext]&publicPath=../"
      },
      {
        test: /\.(gif|jpg|png|ico)(\?v=\d+\.\d+\.\d+)?$/,
        loader: "file-loader?name=assets/[contenthash].[ext]&publicPath=../"
      },
      {
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        loader:
          "url-loader?limit=10000&mimetype=image/svg+xml&name=assets/[name].[ext]&publicPath=../"
      }
    ]
  },
  resolve: {
    alias: {
      styles: path.resolve(__dirname, "src/styles"),
      assets: path.resolve(__dirname, "src/assets"),
      fonts: path.resolve(__dirname, "src/fonts")
    }
  },
  plugins: [
    new TerserPlugin(),
    //new CleanWebpackPlugin(),
    new ExtractCSSChunksPlugin({
      filename: "styles/[name].css",
      chunkFilename: "[id].css"
    }),
    new CopyPlugin([
      { from: "src/js", to: "js" }
    ]),
  ]
};

// eslint-disable-next-line no-undef
module.exports = config;
