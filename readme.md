## eliminar migrations

´´´
find . -path "_/migrations/_.py" -not -name "**init**.py" -delete
find . -path "_/migrations/_.pyc" -delete
´´´

## eliminar **pycache**

´´´
find . | grep -E "(/**pycache**$|\.pyc$|\.pyo$)" | xargs rm -rf
´´´
