const units = {
    Voltage: ["V", "mV", "kV"],
    Current: ["A", "mA", "uA"],
    Power: ["W", "kW", "MW"],
    Energy: ["J", "kJ", "Wh", "kWh"]
};

const category =
    document.getElementById("category");

const fromUnit =
    document.getElementById("from_unit");

const toUnit =
    document.getElementById("to_unit");


// Update dropdown units
function updateUnits() {

    const selected = units[category.value];

    fromUnit.innerHTML = "";
    toUnit.innerHTML = "";

    selected.forEach(unit => {

        fromUnit.add(new Option(unit, unit));

        toUnit.add(new Option(unit, unit));

    });

    toUnit.selectedIndex = 1;
}


// Listen for category changes
category.addEventListener("change", updateUnits);

updateUnits();


// Convert electrical units
async function convert() {

    const value =
        document.getElementById("value").value;

    const result =
        document.getElementById("result");

    if (value.trim() === "") {

        result.textContent = "Please enter a value";

        return;
    }

    try {

        const response = await fetch("/convert", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                category: category.value,

                value: value,

                from_unit: fromUnit.value,

                to_unit: toUnit.value

            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        result.textContent =
            "Result: " + data.result + " " + data.unit;

    }

    catch (error) {

        result.textContent =
            error.message || "Conversion failed";

    }
}