function calculateBill() {
    let size = document.getElementById("size").value.toUpperCase();
    let paperoni = document.getElementById("paperoni").value.toUpperCase();
    let cheese = document.getElementById("cheese").value.toUpperCase();

    let bill = 0;

    // Pizza size price
    if(size === "M") bill = 10;
    else if(size === "L") bill = 15;
    else if(size === "XL") bill = 20;
    else bill = 10; // default M

    // Toppings price
    if(paperoni === "Y") bill += 2;
    if(cheese === "Y") bill += 5;

    // Display result
    document.getElementById("result").innerText =
        `🧾 Bill Summary:\nSize: ${size}\nPaperoni: ${paperoni==='Y'?'Yes':'No'}\nExtra Cheese: ${cheese==='Y'?'Yes':'No'}\n💰 Total: $${bill}`;
}
