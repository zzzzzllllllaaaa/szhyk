import React, { useState } from "react";
import * as Component from "./components"; // 确保引入了你的 Explorer 组件

const Sidebar = () => {
  const [isSidebarVisible, setIsSidebarVisible] = useState(false);

  const toggleSidebarVisibility = () => {
    setIsSidebarVisible(!isSidebarVisible);
  };

  return (
    <>
      <button onClick={toggleSidebarVisibility} style={floatingButtonStyles}>
        📁
      </button>
      <div style={{ ...sidebarStyles, transform: isSidebarVisible ? "translateX(0)" : "translateX(-100%)" }}>
        <button onClick={toggleSidebarVisibility} style={closeButtonStyles}>
          &times;
        </button>
        <div style={explorerContainerStyles}>
          <Component.Explorer />
        </div>
      </div>
    </>
  );
};

const floatingButtonStyles = {
  position: "fixed" as "fixed",
  bottom: "20px",
  left: "20px",
  width: "60px",
  height: "60px",
  backgroundColor: "#007bff",
  color: "#fff",
  borderRadius: "50%",
  border: "none",
  boxShadow: "0px 2px 10px rgba(0,0,0,0.3)",
  cursor: "pointer",
  fontSize: "24px",
  zIndex: 1001,
};

const sidebarStyles = {
  position: "fixed" as "fixed",
  top: "0",
  left: "0",
  width: "80%",
  maxWidth: "300px",
  height: "100%",
  backgroundColor: "#fff",
  boxShadow: "2px 0 5px rgba(0,0,0,0.3)",
  padding: "10px",
  transition: "transform 0.3s ease",
  zIndex: 1000,
};

const closeButtonStyles = {
  position: "absolute" as "absolute",
  top: "10px",
  right: "10px",
  background: "none",
  border: "none",
  fontSize: "24px",
  cursor: "pointer",
};

const explorerContainerStyles = {
  marginTop: "40px", // 确保Explorer组件不会被关闭按钮遮挡
};

export default Sidebar;
