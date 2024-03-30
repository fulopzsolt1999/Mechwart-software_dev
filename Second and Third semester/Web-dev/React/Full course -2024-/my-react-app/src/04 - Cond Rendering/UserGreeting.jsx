import styles from "./UserGreeting.module.css";
import PropTypes from "prop-types";

export default function UserGreeting(props) {
   const welcomeMessage = <h2 className={styles.welcome_message}>Welcome {props.username}</h2>;
   const loginPrompt = <h2 className={styles.login_prompt}>Please log in to continue</h2>;

   return props.isLoggedIn ? welcomeMessage : loginPrompt;
}

UserGreeting.propTypes = {
   isLoggedIn: PropTypes.bool,
   username: PropTypes.string,
};
UserGreeting.defaultProps = {
   isLoggedIn: false,
   username: "Guest",
};
