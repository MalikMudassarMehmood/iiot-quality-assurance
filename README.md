# Development of an Automated Quality Assurance System for the Beverage Industry Using IIoT Technologies

![GitHub repo size](https://img.shields.io/github/repo-size/MalikMudassarMehmood/iiot-quality-assurance)
![GitHub stars](https://img.shields.io/github/stars/MalikMudassarMehmood/iiot-quality-assurance?style=social)
![GitHub issues](https://img.shields.io/github/issues/MalikMudassarMehmood/iiot-quality-assurance)

**Author:** Mudassar Mehmood  
**Affiliation:** National Textile University, Faisalabad, Pakistan  
**Corresponding Author:** malikmudassar0197@gmail.com  

---

## Table of Contents
- [About](#about)
- [Dataset Information](#dataset-information)
- [Code Information](#code-information)
- [Usage Instructions](#usage-instructions)
- [Requirements](#requirements)
- [Methodology](#methodology)
- [Figures](#figures)
- [License & Usage](#license--usage)
- [Getting Help](#getting-help)

---

## About
This project presents the design and implementation of an **Industrial Internet of Things (IIoT)-enabled automated quality assurance system** for beverage production lines.  
The system measures the weight of empty bottles, filled bottles, and final packaged products using load cells and Arduino-based acquisition. Bottles are automatically accepted or rejected based on predefined thresholds. Real-time logging ensures traceability and supports continuous quality improvement.  

This README communicates:  
- What the project does  
- Why the project is useful  
- How users can get started  
- Where users can get help  
- Who maintains the project  

---

## Dataset Information
The dataset contains weight readings for PET bottles at three production stages: empty, filled, and final packaged.

- **Real samples:** 1,000 per category (empty, filled, final)  
- **Synthetic samples:** 9,000 per category, generated using uniform random distribution  
- **Total samples:** 10,000 per category  

**Weight ranges for synthetic data generation:**  
- Empty bottles: 14–20 g  
- Filled bottles: 516–529 g  
- Final packaged bottles: 520–530 g  

**Labels:**  
Each record is labeled with the corresponding inspection stage (`empty`, `filled`, `final`) for classification and analysis.  

**[Download Dataset](data)**

---

## Code Information
The repository includes the following main components:

- **Arduino Scripts:** Read load cell data via HX711 and transmit weights to host computer over USB serial.  
- **Python Scripts:** Receive serial data, apply threshold checks for underfilling, overfilling, or defective caps, log inspection results, and generate reports.  

**[Download Code](Code)**

---

## Usage Instructions

**Hardware Setup:**
1. Connect three IIoT-enabled load cells with HX711 modules to an Arduino UNO.  
2. Place the conveyor system or testing platform for bottle inspection.  

**Software Setup:**
1. Connect Arduino to the workstation via USB.  
2. Run the Arduino sketch to start weight acquisition.  
3. On the host computer, run Python scripts to process thresholds and log results.  

**Data Logging & Analysis:**
- Python scripts save CSV files containing weight values, inspection stage labels, acceptance/rejection decisions, and timestamps.  
- Use the CSV files for plotting, reporting, or machine learning experiments.  

---

## Requirements

**Hardware:**
- Arduino UNO (ATmega328P, 16 MHz)  
- 3 × Load Cells (5 kg capacity)  
- 3 × HX711 modules  
- USB power supply and connecting wires  
- PET bottles (500 ml)  

**Software / Libraries:**
- Python 3.x  
- pyserial (for serial communication)  
- pandas (for CSV logging and manipulation)  
- matplotlib or seaborn (optional, for plotting)  

---

## Methodology
1. **Sensor Integration:** Load cells with HX711 modules capture bottle weights at three stages (empty, post-filling, final capping).  
2. **Data Acquisition:** Arduino UNO collects sensor data and transmits it to a workstation via USB serial.  
3. **Real-Time Data Processing:** Python scripts compare readings against predefined thresholds to detect anomalies.  
4. **Decision-Making:** Bottles are automatically accepted or rejected based on sensor readings.  
5. **Logging & Traceability:** Each stage logs outcomes, timestamps, and weight values for auditability.  
6. **Synthetic Data Generation:** Uniform random data is used to expand real measurements to 10,000 samples per category.  
7. **Performance Evaluation:** The system was tested for processing times per stage and compared against traditional automated inspection methods.  

---

## Figures
**Add images to your repository in `images/` folder and link here:**

![System Architecture](images/system_architecture.png)  
*Fig 1: IIoT-enabled Quality Assurance System Architecture*

![Process Flow](images/flowchart.png)  
*Fig 2: Process Flow of Bottle Inspection*

---

## License & Usage
This project and dataset are created by **Mudassar Mehmood** for research purposes.  

- **License:** MIT (adapt as required)  
- **Usage:** You are free to use, modify, or reference this work in your own projects, provided you credit the author.  
- **Contributions:** Pull requests are welcome. Include clear descriptions of changes and ensure compatibility with hardware and scripts.  
- **Issues:** Report bugs or feature requests via the GitHub issues page.  

---

## Getting Help
For questions, issues, or feedback, contact the author:

**Mudassar Mehmood**  
Email: malikmudassar0197@gmail.com

