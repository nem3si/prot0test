<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>Prototype Pollution Tester</h1>


<p>prot0test is a tool that allows you to test a web page for prototype pollution vulnerabilities. Prototype pollution is a security vulnerability that occurs when an attacker can inject properties into existing objects, leading to unexpected or malicious behavior.</p>

<p><strong>Note:</strong> This tool provides a basic demonstration of prototype pollution testing and may not detect all variations of the vulnerability.</p>

<h2>How to Use</h2>

<ol>
<li>Clone the repository and navigate to the project directory.</li>
<li>Install the required dependencies by running <code>pip install -r requirements.txt</code>.</li>
<li>Run the script using the following command:</li>
</ol>

<pre><code>python prototype_pollution_tester.py
</code></pre>

<p>Follow the prompts to enter the URL of the web page you want to test.</p>

<p>The script will perform prototype pollution testing and provide the results.</p>

<h2>Dependencies</h2>

<ul>
<li><code>asyncio</code></li>
<li><code>requests</code></li>
<li><code>py_mini_racer</code></li>
</ul>

<h2>Contributing</h2>

<p>Contributions are welcome! If you find any issues or want to enhance the tool, feel free to submit a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
