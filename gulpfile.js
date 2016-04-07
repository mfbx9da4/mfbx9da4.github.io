'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');

gulp.task('sass-main', function () {
  return gulp.src('./_scss/main.scss')
	.pipe(sourcemaps.init())
	.pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
	.pipe(sourcemaps.write('./maps'))
    .pipe(gulp.dest('./css/'));
});

gulp.task('sass-landing-page', function () {
  return gulp.src('./_landing-page-src/scss/landing-page.scss')
	.pipe(sourcemaps.init())
	.pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
	.pipe(sourcemaps.write('./css/maps'))
    .pipe(gulp.dest('./css/'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./_scss/**/*.scss', ['sass-main']);
  gulp.watch('./_landing-page-src/scss/**/*.scss', ['sass-landing-page']);
});
