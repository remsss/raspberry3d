echo off

kill -9 $(sudo lsof -t -i:20078)
