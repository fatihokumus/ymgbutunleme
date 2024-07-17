const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.json());

app.post('/predict', async (req, res) => {
  const { firstName, lastName } = req.body;
  try {
    const response = await axios.post('http://localhost:5000/predict', { firstName, lastName });
    res.json(response.data);
  } catch (error) {
    res.status(500).send('Error predicting origin');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});