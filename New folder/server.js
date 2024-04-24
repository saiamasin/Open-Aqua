const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000; // You can change the port if needed

http.createServer((req, res) => {
    const filePath = path.join(__dirname, 'index.html');

    fs.readFile(filePath, (err, data) => {
        if (err) {
            res.writeHead(500);
            return res.end('Error loading index.html');
        }

        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
}).listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}/`);
});
