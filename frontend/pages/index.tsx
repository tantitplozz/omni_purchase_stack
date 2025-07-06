import React, { useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("");
  const handleBuy = async () => {
    setStatus("Processing...");
    const res = await fetch("/api/run_purchase", {
      method: "POST",
      body: JSON.stringify({
        target: "apple.com/th",
        product: {
          name: "iPhone 16 Pro Max",
          color: "White",
          storage: "256GB",
          pickup: "CentralWorld",
        },
        card: {
          name: "Suthawan Siriratusdorn",
          address:
            "787/791 Happy Condo Ladprao, Building G, Soi Ladprao 101, Khlong Chaokhunsing Wang Thonglang, Bangkok 10310",
          number: "4417701003947464",
          exp: "07/25",
          cvv: "768",
          tel: "0627046442",
          email: "mogo.suthawan@gmail.com",
        },
        steps: [
          {
            agent: "browser",
            task: "open_url",
            url: "https://www.apple.com/th/shop/buy-iphone/iphone-16-pro",
          },
          { agent: "search", task: "find_product", keyword: "iPhone 16 Pro Max สีขาว 256GB" },
          { agent: "cart", task: "add_to_cart", selector: "#add-to-cart" },
          { agent: "checkout", task: "checkout_form" },
        ],
        notify: "telegram",
      }),
    });
    const data = await res.json();
    setStatus(JSON.stringify(data));
  };
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">God-Tier iPhone 16 Pro Max AutoBuy</h1>
      <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={handleBuy}>
        สั่งซื้อทันที
      </button>
      <pre className="mt-6">{status}</pre>
    </div>
  );
}
