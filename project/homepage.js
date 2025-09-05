import React, { useState } from 'react';
import './HomePage.css'; // We'll create this CSS file next

const HomePage = () => {
  const [isProfileOpen, setIsProfileOpen] = useState(false);
  const userData = {
    username: "JohnDoe",
    email: "johndoe@example.com",
    joinDate: "January 15, 2023",
    role: "Premium Member"
  };

  const toggleProfile = () => {
    setIsProfileOpen(!isProfileOpen);
  };

  return (
    <div className="homepage-container">
      <header className="homepage-header">
        <h1>Welcome to Our Application</h1>
        <p>Your one-stop solution for all needs</p>
      </header>
      
      <main className="homepage-main">
        <div className="content-section">
          <h2>Featured Content</h2>
          <p>This is the main content area of your homepage. You can add any components, text, or media here.</p>
        </div>
      </main>
      
      {/* Profile Circle */}
      <div className="profile-container">
        <div 
          className="profile-circle"
          onClick={toggleProfile}
        >
          {userData.username.charAt(0)}
        </div>
        
        {isProfileOpen && (
          <div className="profile-dropdown">
            <div className="profile-header">
              <div className="profile-icon-large">
                {userData.username.charAt(0)}
              </div>
              <h3>{userData.username}</h3>
              <p>{userData.email}</p>
            </div>
            <div className="profile-details">
              <div className="detail-item">
                <span className="label">Member since:</span>
                <span>{userData.joinDate}</span>
              </div>
              <div className="detail-item">
                <span className="label">Status:</span>
                <span>{userData.role}</span>
              </div>
            </div>
            <div className="profile-actions">
              <button className="profile-btn">View Profile</button>
              <button className="profile-btn">Settings</button>
              <button className="profile-btn logout">Log Out</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default HomePage;